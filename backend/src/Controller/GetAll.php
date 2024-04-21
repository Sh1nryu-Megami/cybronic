<?php


require 'vendor/autoload.php';

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class GetAll extends AbstractController
{
    #[Route('api/getall', methods: ['GET', 'POST'])]
    public function getAll()
    {
        $redis = new Predis\Client();
        $x_pos = $redis->get('x');
        $y_pos = $redis->get('y');
        $posts = array($x_pos, $y_pos);
        return $this->json($posts);
    }
}
