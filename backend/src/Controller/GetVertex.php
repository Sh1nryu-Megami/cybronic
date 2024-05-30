<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Predis;
use Exception;

class GetVertex extends AbstractController
{
    #[Route('api/getvertex/{mac}/{x}/{y}', methods: ['GET', 'POST'])]
    public function getMacByName(string $mac, float $x, float $y): Response
    {
      $host = 'localhost';

      if (getenv('DBHOST') !== false) {
        $host = getenv('DBHOST');
      }
  
      $redis = new Predis\Client(['host' => $host]);
      $redis->hset('users', $mac, json_encode(['x' => $x, 'y' => $y]));
      return $this->json('ok');
    }
}