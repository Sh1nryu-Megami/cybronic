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
            $path = BFS($n + 1, $graph, $point, $mac);
            $post = array();
            foreach ($path as $v) {
                $post[] = array('x' => $graph[$v]['x'], 'y' => $graph[$v]['y']);
            }

            if (count($post) >= 2) {
                $delta_x = abs($post[1]['x'] - $post[0]['x']);
                $delta_y = abs($post[1]['y'] - $post[0]['y']);

                if ($delta_x > $delta_y) {
                    $post[0]['y'] = $post[1]['y'];
                } else {
                    $post[0]['x'] = $post[1]['x'];
                }
            }
            return $this->json($post);
        }
        return $this->json('error');
    }
}
