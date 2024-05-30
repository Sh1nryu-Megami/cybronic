import $ from 'jquery';

export function getTouchStart(data, layout) {
  return function (event) {
    event.preventDefault();
    event.stopPropagation();

    let map_elem = $('#map');
    const mapOffset = map_elem.offset();
    const mapWidth = map_elem.width();

    let move_elem = $('.move');
    const offset = move_elem.offset();
    data.value.left = offset.left;
    data.value.top = offset.top;
    data.value.scx = event.touches[0].clientX;
    data.value.scy = event.touches[0].clientY;
    
    const ratio = mapWidth / layout.value.width;
    data.value.rx = (data.value.x - mapOffset.left) / ratio;
    data.value.ry = (data.value.y - mapOffset.top) / ratio;
  }
}

export function getTouchMove(data) {
  return function (event) {
    event.preventDefault();
    event.stopPropagation();

    const width = $('.move').width();
    
    data.value.x = data.value.left + event.touches[0].clientX - data.value.scx + width / 2;
    data.value.y = data.value.top + event.touches[0].clientY - data.value.scy + width / 2;
    console.log('move');
  }
}