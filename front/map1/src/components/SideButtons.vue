<script setup>
import $ from 'jquery'
import PlusButton from '/src/assets/PlusButton.svg';
import MinusButton from '/src/assets/MinusButton.svg';

const props = defineProps(['update']);

function zoom(delta) {
	let currOffset = $("#map");
	let point = $('.personPoint');

	if (point.length == 0) {
		return;
	}

	const pointOffset = point.offset();
	console.log(pointOffset)
	const pointW = point.width();
	const pointH = point.height();
	const midX = (pointOffset.left + pointW / 2);
	const midY = (pointOffset.top + pointH / 2);

	const offset = currOffset.offset();
	const mapX = offset.left;
	const mapY = offset.top;
	const mapW = currOffset.width();
	const mapH = currOffset.height();

	const ratioW = delta * mapW * 0.2;
	const ratioH = mapH / mapW * ratioW;
	const newWidth = mapW + ratioW;
	const newHeight = mapH + ratioH;

	if (newWidth > 3300 && newHeight > 1368 && newWidth < 230 && newHeight < 100) {
		return;
	}

	const midXratio = (midX - mapX) / mapW;
	const midYratio = (midY - mapY) / mapH;
	const midOffsetX = midXratio * newWidth;
	const midOffsetY = midYratio * newHeight;
	const newMapPosX = midX - midOffsetX;
	const newMapPosY = midY - midOffsetY;

	currOffset.offset({ left: newMapPosX, top: newMapPosY });
	currOffset.width(newWidth);
	currOffset.height(newHeight);

	props.update();
}

function zoomPlus() {
	zoom(1);
}

function zoomMinus() {
	zoom(-1)
}

</script>

<template>
	<div :class="$style.side_buttons">
		<button :class="$style.button" @click="zoomPlus">
			<img :src="PlusButton" alt="zoom in" />
		</button>
		<button :class="$style.button" @click="zoomMinus">
			<img :src="MinusButton" alt="zoom out" />
		</button>
	</div>
</template>

<style module lang='scss'>
@use '/src/colors';

.side_buttons {
	display: flex;
	position: absolute;
	right: 0;
	top: calc(50% - 45px);
	margin-right: 2%;
	flex-direction: column;
	align-items: end;

	&>button {
		margin-bottom: 10px;
	}

	&>button:last-child {
		margin-bottom: 0;
	}
}

.button {
	height: 40px;
	width: 40px;
	border: none;
	background-color: #00000000;

	&>img {
		width: 100%;
	}
}
</style>