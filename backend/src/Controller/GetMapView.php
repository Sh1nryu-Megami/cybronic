<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Predis;

class GetMapView extends AbstractController
{
    #[Route('api/getview', methods: ['GET', 'POST'])]
    public function getAll(): Response
    {
        $redis = new Predis\Client();
        $view_path = $redis->get('view');
        $view_content = file_get_contents($view_path);

        return new Response($view_content, 200, ['Content-Type' => 'image/svg+xml']);
    }
}