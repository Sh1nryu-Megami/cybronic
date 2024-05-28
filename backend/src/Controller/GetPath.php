<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Exception;


class GetPath extends AbstractController
{
    #[Route('api/getpath/{mac}/{point}', methods: ['GET', 'POST'])]
    public function getPath($mac, $point): Response
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
        if (array_key_exists($point, $graph) && addToNearest($graph, $mac)) {
            return $this->json(BFS($n + 1, $graph, $point, $mac));
        }
        return $this->json(['error']);
    }
}
