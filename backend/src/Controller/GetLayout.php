<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Predis;

class GetLayout extends AbstractController
{
    #[Route('api/getlayout', methods: ['GET', 'POST'])]
    public function getAll(): Response
    {
        $redis = new Predis\Client();
        $layout_path = $redis->get('map');
        $layout_content = file_get_contents($layout_path);
        $layout = json_decode($layout_content, true);
        $answer = [
            "width" => $layout['bounds']['width'],
            "height" => $layout['bounds']['height'],
        ];
        return $this->json($answer);
    }
}