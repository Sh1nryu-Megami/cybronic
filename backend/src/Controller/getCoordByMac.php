<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Predis;
use Exception;

class getCoordByMac extends AbstractController
{
	#[Route('api/getcoordbymac/{mac}', methods: ['GET', 'POST'])]
	public function getAll($mac): Response
	{
		$host = 'localhost';

		if (getenv('DBHOST') !== false) {
			$host = getenv('DBHOST');
		}

		$redis = new Predis\Client(['host' => $host]);
		$users = $redis->hgetall('users');
		try {
			$post = $users[$mac];
		} catch (Exception $e) {
			return $this->json($e);
		}
		return $this->json($post);
	}
}
