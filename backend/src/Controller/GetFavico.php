<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;


class GetFavico extends AbstractController
{
    #[Route('/favicon.ico', methods: ['GET', 'POST'])]
    public function getFavico(): Response
    {
      $index = file_get_contents('../data/dist/favicon.ico');
      $resp = new Response($index);
      $resp->setStatusCode(200);
      $resp->headers->set('Content-Type', 'image/x-icon');
      return $resp;
    }
}