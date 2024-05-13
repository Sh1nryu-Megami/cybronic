<?php

/** функция находит ближайшую к пользователю вершину
 * и добавляет к ней фиктивную вершину-пользователя
 * @param string $mac Mac-адрес пользователя
 * @param mixed &$graph Граф карты
 * @return void
 */
function addToNearest(&$graph, string $mac)
{

    $redis = new Predis\Client();
    $start_point = json_decode($redis->hgetall('users')[$mac], true);

    $start_x = $start_point['x'];
    $start_y = $start_point['y'];
    // закоментил потому что не вижу смысла в поиске двух ближайших, если что - спрашивай
    // $dist_to_vertexes = array_fill_keys(array_keys($graph), 10000000);  // тут должно быть число равное размеру карты
    // foreach ($graph as $id => $vert) {
    //     $v_x = $vert['x'];
    //     $v_y = $vert['y'];
    //     $curr_dist = sqrt(($v_x - $start_x) ** 2 + ($v_y - $start_y) ** 2);
    //     $dist_to_vertexes[$id] = $curr_dist;
    // }
    // asort($dist_to_vertexes);
    $nearest_dist = 1000000000;  // тут должно быть число равное размеру карты
    $neares_id = -1;
    foreach ($graph as $id => $vert) {
        $v_x = $vert['x'];
        $v_y = $vert['y'];
        $curr_dist = sqrt(($v_x - $start_x) ** 2 + ($v_y - $start_y) ** 2);
        if ($curr_dist < $nearest_dist) {
            $nearest_dist = $curr_dist;
            $neares_id = $id;
        }
    }
    $graph[$mac]['x'] = $start_x;
    $graph[$mac]['y'] = $start_y;
    $graph[$mac]['adjacent'][] = $neares_id;
    $graph[$neares_id]['adjacent'][] = $mac;
}
