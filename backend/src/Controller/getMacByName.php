<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Exception;

class getMacByName extends AbstractController
{
    #[Route('api/getmacbyaaaa/{name}', methods: ['GET', 'POST'])]
    public function getMacByName($req_name): Response
    {
        try {
            $f_json = file_get_contents('../data/nameToMac.json');
            $content = json_decode($f_json, true);
            $mapping = $content['graph'];
        } catch (Exception $e) {
            return $this->json('JSON exception',  $e->getMessage());
        }
        foreach ($mapping as $name => $mac) {
            if ($req_name == $name) {
                return $this->json($mac);
            }
        }
        return $this->json("Error", "No matching");
    }
}
