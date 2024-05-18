<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class GetMapView extends AbstractController
{
    #[Route('api/getview', methods: ['GET', 'POST'])]
    public function getAll(): Response
    {
        $view_content = file_get_contents('../data/view.svg');

        return new Response($view_content, 200, ['Content-Type' => 'image/svg+xml']);
    }
}