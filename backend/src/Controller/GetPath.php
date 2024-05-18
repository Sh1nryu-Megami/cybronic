<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Exception;


class GetPath extends AbstractController
{
    #[Route('api/getpath', methods: ['GET', 'POST'])]
    public function getPath(): Response
    {
        try {
            // путь до jsona с картой и графом
            $f_json = file_get_contents('../data/layout.json');
            $content = json_decode($f_json, true);
            $graph = $content['graph'];
        } catch (Exception $e) {
            return $this->json('JSON exception',  $e->getMessage());
        }
        $n = count($content['graph']);

        // тут должен быть mac
        addToNearest($graph, '299');

        return $this->json(BFS($n + 1, $graph, 'room7', '299'));  //вместо room7 - пункт назначения
    }
}
