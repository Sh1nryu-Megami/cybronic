import $ from 'jquery'

export function setStartPosWrapper(position_data) {
  function setStartPos(event) {
    event.preventDefault()
    let fingers = []
    for (let touch of event.touches) {
      let x = touch.pageY
      let y = touch.pageX
      fingers.append({ x, y })
    }
    position_data.startFingers = fingers
    if (!position_data.touched) {
      let offset = $(position_data.img_ref)
      position_data.map.x = offset.offset().left
      position_data.map.y = offset.offset().top
      position_data.map.width = offset.width()
      position_data.map.height = offset.height()
    }
    position_data.touched = true
  }
  return setStartPos
}

export function setEndPosWrapper(position_data) {
  function setEndPos(event) {
    event.preventDefault()
    position_data.touched = false
  }
  return setEndPos
}

export function setCancelPosWrapper(position_data) {
  function setCancelPos(event) {
    event.preventDefault()
    position_data.touched = false
  }
  return setCancelPos
}

export function setMovePosWrapper(position_data) {
  function setMovePos(event) {
    event.preventDefault()
    // let currMap = {};
    let currOffset = $(position_data.img_ref)
    // currMap.x = curOffset.offset().left;
    // currMap.y = curOffset.offset().top;
    // currMap.w = curOffset.width();
    // currMap.h = curOffset.height();
    let fingers = []
    for (let touch of event.touches) {
      let x = touch.pageY
      let y = touch.pageX
      fingers.append({ x, y })
    }
    if (position_data.startFingers.length >= 2) {
      let oldFirstX = position_data.startFingers[0].x
      let oldFirstY = position_data.startFingers[0].y
      let oldSecondX = position_data.startFingers[1].x
      let oldSecondY = position_data.startFingers[1].y
      let oldMidX = (oldFirstX + oldSecondX) / 2
      let oldMidY = (oldFirstY + oldSecondY) / 2

      let newFirstX = fingers[0].x
      let newFirstY = fingers[0].y
      let newSecondX = fingers[1].x
      let newSecondY = fingers[1].y
      let newMidX = (newFirstX + newSecondX) / 2
      let newMidY = (newFirstY + newSecondY) / 2

      let shiftX = newMidX - oldMidX
      let shiftY = newMidY - oldMidY

      try {
        let ratio =
          Math.sqrt((newSecondX - newFirstX) ** 2 + (newSecondY - newFirstY) ** 2) /
          Math.sqrt((oldSecondX - oldFirstX) ** 2 + (oldSecondY - oldFirstY) ** 2)
      } catch (e) {
        console.log(e)
        return
      }
      shiftX *= ratio
      shiftY *= ratio

      let tmpMap = Object.assign({}, position_data.map)
      tmpMap.w *= ratio
      tmpMap.h *= ratio
      let screenWidthOffset = (tmpMap.w - position_data.map.w) / 2
      let screenHeightOffset = (tmpMap.h - position_data.map.h) / 2
      shiftX -= screenWidthOffset
      shiftY -= screenHeightOffset
      currOffset.offset({ left: shiftX, top: shiftY })
      curOffset.width(position_data.map.w * ratio)
      curOffset.height(position_data.map.h * ratio)
    }
    if (position_data.startFingers.length == 1) {
      let oldX = position_data.startFingers[0].x
      let oldY = position_data.startFingers[0].y
      let newX = fingers[0].x
      let newY = fingers[0].y
      let shiftX = newX - oldX
      let shiftY = newY - oldY
      currOffset.offset({ left: shiftX, top: shiftY })
    }
  }
  return setMovePos
}
