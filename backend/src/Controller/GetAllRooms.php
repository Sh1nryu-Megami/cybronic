<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Exception;

class GetAllRooms extends AbstractController
{
    #[Route('api/getallrooms', methods: ['GET', 'POST'])]
    public function getAllRooms(): Response
    {
        try {
            // путь до jsona с картой и графом
            $f_json = file_get_contents('D:\Reposits\cybronic\math_module\tools\map_create\output\graph5.json');
            $content = json_decode($f_json, true);
            $graph = $content['graph'];
        } catch (Exception $e) {
            return $this->json('JSON exception',  $e->getMessage());
        }

        $posts = array();
        foreach ($graph as $id => $vert) {
            if (str_starts_with($id, 'room')) {
                $posts[$id]['x'] = $vert['x'];
                $posts[$id]['y'] = $vert['y'];
            }
        }
        return $this->json($posts);
    }
}
