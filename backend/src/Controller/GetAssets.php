<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;


class GetAssets extends AbstractController
{
    #[Route('/assets/{id}', methods: ['GET', 'POST'])]
    public function getFavico($id): Response
    {
      $index = file_get_contents('../data/dist/assets/' . $id);
      $resp = new Response($index);
      $resp->setStatusCode(200);
      $file_path = pathinfo($id);

      if ($file_path['extension'] == 'js') {
        $resp->headers->set('Content-Type', 'text/javascript');
      } else if ($file_path['extension'] == 'css') {
        $resp->headers->set('Content-Type', 'text/css');
      } else {
        $resp->headers->set('Content-Type', mime_content_type('../data/dist/assets/' . $id));
      }
      return $resp;
    }
}