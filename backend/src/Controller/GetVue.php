<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;


class GetVue extends AbstractController
{
    #[Route('/', methods: ['GET', 'POST'])]
    public function getVue(): Response
    {
      $index = file_get_contents('../data/dist/index.html');
      $resp = new Response($index);
      $resp->setStatusCode(200);
      return $resp;
    }
}