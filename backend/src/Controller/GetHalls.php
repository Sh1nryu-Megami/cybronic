<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class GetHalls extends AbstractController
{
    #[Route('api/gethalls', methods: ['GET', 'POST'])]
    public function getHalls(): Response
    {
        $layout_content = file_get_contents('../data/layout.json');
        $layout = json_decode($layout_content, true);
        $answer = $layout['halls'];
        return $this->json($answer);
    }
}