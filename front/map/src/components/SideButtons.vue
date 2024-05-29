<script setup>
import $ from 'jquery'

function zoomPlus(event) {
	let currOffset = $("#map");
	let offset = currOffset.offset();
	let mapX = offset.left;
	let mapY = offset.top;
	let mapW = currOffset.width();
	let mapH = currOffset.height();

	let ratioW = mapW * 0.2;
	let ratioH = mapH / mapW * ratioW;
	let newWidth = mapW + ratioW;
	let newHeight = mapH + ratioH;
	if (newWidth > 3300 && newHeight > 1368) {
		return;
	}
	let newMapPosX = mapX - ratioW;
	let newMapPosY = mapY - ratioH;

	currOffset.offset({ left: newMapPosX, top: newMapPosY });
	currOffset.width(newWidth)
	currOffset.height(newHeight)
}

function zoomMinus(event) {
	let currOffset = $("#map");
	let offset = currOffset.offset();
	let mapX = offset.left;
	let mapY = offset.top;
	let mapW = currOffset.width();
	let mapH = currOffset.height();

	let ratioW = -mapW * 0.2;
	let ratioH = mapH / mapW * ratioW;
	let newWidth = mapW + ratioW;
	let newHeight = mapH + ratioH;
	if (newWidth < 230 && newHeight < 100) {
		return;
	}
	let newMapPosX = mapX - ratioW;
	let newMapPosY = mapY - ratioH;

	currOffset.offset({ left: newMapPosX, top: newMapPosY });
	currOffset.width(newWidth)
	currOffset.height(newHeight)
}

</script>

<template>
	<div :class="$style.side_buttons">
		<button :class="$style.plus_button" @click="zoomPlus"></button>
		<button :class="$style.minus_button" @click="zoomMinus"></button>
	</div>
</template>

<style module lang='scss'>
@use '/src/colors';

.side_buttons {
	display: flex;
	position: absolute;
	right: 0;
	top: 50%;
	margin-right: 2%;
	flex-direction: column;
	align-items: end;
}

.plus_button {
	height: 40px;
	width: 40px;
	border: none;
	background-color: colors.$menu_bg;
	background-image: url("../assets/PlusButton.svg");
	background-size: cover;
}

.minus_button {
	height: 40px;
	width: 40px;
	border: none;
	background-color: colors.$menu_bg;
	margin-top: 30%;
	background-image: url("../assets/MinusButton.svg");
	background-size: cover;
}
</style>