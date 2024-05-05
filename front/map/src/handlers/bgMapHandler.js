import $ from 'jquery'

export function setStartPosWrapper(position_data) {
  function setStartPos(event) {
    event.preventDefault()
    let fingers = []
    for (let touch of event.touches) {
      let x = touch.pageX 
      let y = touch.pageY 
      fingers.push({ x, y })
    }
    position_data.value.startFingers = fingers;
    console.log("Tstart");
    console.log(fingers);

    if (position_data.value.touched == false) {
      let map = $("#map");
      let offset = map.offset();
      position_data.value.map.x = offset.left;
      position_data.value.map.y = offset.top;
      position_data.value.map.w = map.width();
      position_data.value.map.h = map.height();
      console.log("Set Map");
    }
    position_data.value.touched = true;
  }
  return setStartPos
}

export function setEndPosWrapper(position_data) {
  function setEndPos(event) {
    event.preventDefault()
    console.log("TEnd");

    if (event.touches.length == 0) {
      position_data.value.touched = false;
      console.log("TEnd Set t false");
    }
  }
  return setEndPos
}

export function setCancelPosWrapper(position_data) {
  function setCancelPos(event) {
    event.preventDefault()
    console.log("TCancel");

    if (event.touches.length == 0) {
      position_data.value.touched = false;
      console.log("TCancel Set t false");
    }
  }
  return setCancelPos
}

export function setMovePosWrapper(position_data) {
  function setMovePos(event) {
    event.preventDefault();
    console.log("TMove");

    if (position_data.value.touched == false) {
      console.log("TMove return");
      return;
    }

    let currOffset = $("#map");
    let fingers = []
    for (let touch of event.touches) {
      let x = touch.pageX
      let y = touch.pageY
      fingers.push({ x, y })
    }
    if (position_data.value.startFingers.length >= 2) {
      let oldFirstX = position_data.value.startFingers[0].x
      let oldFirstY = position_data.value.startFingers[0].y
      let oldSecondX = position_data.value.startFingers[1].x
      let oldSecondY = position_data.value.startFingers[1].y
      let oldMidX = (oldFirstX + oldSecondX) / 2
      let oldMidY = (oldFirstY + oldSecondY) / 2

      let newFirstX = fingers[0].x
      let newFirstY = fingers[0].y
      let newSecondX = fingers[1].x
      let newSecondY = fingers[1].y
      let newMidX = (newFirstX + newSecondX) / 2
      let newMidY = (newFirstY + newSecondY) / 2

      // let shiftX = newMidX - oldMidX;
      // let shiftY = newMidY - oldMidY;
      let ratio;
      try {
        ratio = Math.sqrt((newSecondX - newFirstX) ** 2 + (newSecondY - newFirstY) ** 2) /
          Math.sqrt((oldSecondX - oldFirstX) ** 2 + (oldSecondY - oldFirstY) ** 2)
      } catch (e) {
        console.log(e);
        return;
      }

      let newWidth = position_data.value.map.w * ratio;
      let newHeight = position_data.value.map.h * ratio;
      let midXratio = (oldMidX - position_data.value.map.x) / position_data.value.map.w;
      let midYratio = (oldMidY - position_data.value.map.y) / position_data.value.map.h;
      let midOffsetW = newWidth * midXratio;
      let midOffsetH = newHeight * midYratio;

      let newMapPosX = -midOffsetW + oldMidX;
      let newMapPosY = -midOffsetH + oldMidY;

      newMapPosX += newMidX - oldMidX;
      newMapPosY += newMidY - oldMidY;
      // shiftX *= ratio;
      // shiftY *= ratio;

      // let screenWidthOffset = position_data.value.map.w * (ratio - 1) / 2;
      // let screenHeightOffset = position_data.value.map.h * (ratio - 1) /2;
      // shiftX -= screenWidthOffset;
      // shiftY -= screenHeightOffset;
      currOffset.offset({ left: newMapPosX, top: newMapPosY });
      currOffset.width(newWidth)
      currOffset.height(newHeight)
    }
    if (position_data.value.startFingers.length == 1) {
      let oldX = position_data.value.startFingers[0].x
      let oldY = position_data.value.startFingers[0].y
      let newX = fingers[0].x
      let newY = fingers[0].y
      let shiftX = newX - oldX
      let shiftY = newY - oldY
      currOffset.offset({ left: shiftX + position_data.value.map.x, top: shiftY + position_data.value.map.y })
    }
  }
  return setMovePos
}
