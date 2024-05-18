<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class GetLayout extends AbstractController
{
    #[Route('api/getlayout', methods: ['GET', 'POST'])]
    public function getAll(): Response
    {
        $layout_content = file_get_contents('../data/layout.json');
        $layout = json_decode($layout_content, true);
        $answer = [
            "width" => $layout['bounds']['width'],
            "height" => $layout['bounds']['height'],
        ];
        return $this->json($answer);
    }
}