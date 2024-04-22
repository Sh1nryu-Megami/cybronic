import time


class Store:
  def __init__(self, config, layout):
    self._history = {}
    self._history_interval = config['HISTORY_INTERVAL']
    self._positions = {}
    self._layout = layout

  def _shift(self, mc: str, lighthouse: str) -> bool:
    if mc not in self._positions:
      self._positions[mc] = {
        'x': 0,
        'y': 0,
        'points': [lighthouse]
      }
      return False
    else:
      position = self._positions[mc]
      if len(position['points']) != 2:
        position['points'].append(lighthouse)
        return False
      
      cur_dis = self._history[(mc, lighthouse)]['average']
      point1 = self._history[(mc, position['points'][0])]['average']
      point2 = self._history[(mc, position['points'][1])]['average']

      if cur_dis < point1:
        position['points'][0] = lighthouse
        point1 = cur_dis
      elif cur_dis < point2:
        position['points'][1] = lighthouse
        point2 = cur_dis
      else:
        return False
    
    return True


  def _calculate(self, mc: str) -> None:
    position = self._positions[mc]

    if len(position['points']) != 2:
      return
    
    d1_obj = self._layout['lighthouses'][position['points'][0]]
    d2_obj = self._layout['lighthouses'][position['points'][1]]
    d1 = self._history[(mc, position['points'][0])]['average']
    d2 = self._history[(mc, position['points'][1])]['average']
    x1 = d1_obj['x']
    y1 = d1_obj['y']
    x2 = d2_obj['x']
    y2 = d2_obj['y']

    if (x1 - x2) ** 2 + (y1 - y2) ** 2 >= (d1 + d2) ** 2:
      lh_dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
      d1_x = d1 * (x2 - x1) / lh_dist
      d1_y = d1 * (y2 - y1) / lh_dist
      d2_x = d2 * (x1 - x2) / lh_dist
      d2_y = d2 * (y1 - y2) / lh_dist

      d1_bound_x = x1 + d1_x
      d1_bound_y = y1 + d1_y
      d2_bound_x = x2 + d2_x
      d2_bound_y = y2 + d2_y

      x_pre = (d1_bound_x + d2_bound_x) / 2
      y_pre = (d1_bound_y + d2_bound_y) / 2
    else:
      E = (d1 ** 2 - d2 ** 2 + x2 ** 2 + y2 ** 2 - x1 ** 2 - y1 ** 2) / (2 * (y2 - y1))
      C = (x2 - x1) / (y2 - y1)
      a = 1 + C ** 2
      b = -2 * (x1 + E * C - C * y1)
      c = x1 ** 2 + E ** 2 - 2 * E * y1 + y1 ** 2 - d1 ** 2
      
      D = b ** 2 - 4 * a * c
      x_pre_1 = (-b + D ** 0.5) / (2 * a)
      x_pre_2 = (-b - D ** 0.5) / (2 * a)
      y_pre_1 = E - C * x_pre_1
      y_pre_2 = E - C * x_pre_2

      m_x = x_pre_1
      m_y = y_pre_1
      p_x = x1
      p_y = y1
      b_x = x_pre_2 - x_pre_1
      b_y = y_pre_2 - y_pre_1
      a_x = x2 - x1
      a_y = y2 - y1

      delta = - b_x * a_y + a_x * b_y
      t_1 = (-(p_x - m_x) * a_y + (p_y - m_y) * a_x) / delta

      x_pre = m_x + t_1 * b_x
      y_pre = m_y + t_1 * b_y
    
    if d1_obj['hall'] == d2_obj['hall']:
      hall = d1_obj['hall']
    else:
      d1_hall = self._layout['halls'][d1_obj['hall']]
      d2_hall = self._layout['halls'][d2_obj['hall']]
      
      if d1_obj['hall'].endswith('_hor'):
        d1_dist = abs(y_pre - d1_hall['baseline'])
      else:
        d1_dist = abs(x_pre - d1_hall['baseline'])

      if d2_obj['hall'].endswith('_hor'):
        d2_dist = abs(y_pre - d2_hall['baseline'])
      else:
        d2_dist = abs(x_pre - d2_hall['baseline'])

      if d1_dist < d2_dist:
        hall = d1_obj['hall']
      else:
        hall = d2_obj['hall']
    
    if hall.endswith('_hor'):
      position['x'] = x_pre
      position['y'] = self._layout['halls'][hall]['baseline']
    elif hall.endswith('_vert'):
      position['x'] = self._layout['halls'][hall]['baseline']
      position['y'] = y_pre

  
  def add(self, mc: str, lighthouse: str, distance: float) -> dict:
    scale = self._layout['bounds']['scale']
    distance = distance / scale

    if (mc, lighthouse) not in self._history:
      self._history[(mc, lighthouse)] = {
        'distance': [{
          'distance': distance,
          'time': time.time()
        }],
        'last_time': time.time(),
        'average': distance
      }
    else:
      item = self._history[(mc, lighthouse)]
      cur_time = time.time()
      item['distance'].append({
        'distance': distance,
        'time': cur_time,
      })

      if cur_time - item['last_time'] > self._history_interval:
        for idx, dest_item in enumerate(item['distance']):
          if cur_time - dest_item['time'] <= self._history_interval:
            index = idx
            break
        
        item['distance'] = item['distance'][index:]
        item['last_time'] = item['distance'][0]['time']
      
      item['average'] = sum(dest_item['distance'] for dest_item in item['distance']) / len(item['distance'])
    
    if self._shift(mc, lighthouse):
      self._calculate(mc, lighthouse)
      return self._positions[mc]
    else:
      return {
        'x': -1,
        'y': -1,
      }

