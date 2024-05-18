<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Predis;

class GetAllFromRedis extends AbstractController
{
    #[Route('api/getall', methods: ['GET', 'POST'])]
    public function getAll(): Response
    {
        $host = 'localhost';

        if (getenv('DBHOST') !== false) {
            $host = getenv('DBHOST');
        }

        $redis = new Predis\Client(['host' => $host]);
        $keys = $redis->keys('users');
        $posts = array();
        foreach ($keys as $key) {
            $posts[] = $redis->hgetall($key);
        }
        return $this->json($posts);
    }
}
