<?php

namespace App\Controller;


use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Exception;

class getMacByName extends AbstractController
{
    #[Route('api/getmacbyaaaa/{req_name}', methods: ['GET', 'POST'])]
    public function getMacByName(string $req_name): Response
    {
        try {
            $f_json = file_get_contents('../data/nameToMac.json');
            $mapping = json_decode($f_json, true);
        } catch (Exception $e) {
            return $this->json(array('error' =>  $e->getMessage()));
        }
        foreach ($mapping as $name => $mac) {
            if ($req_name == $name) {
                return $this->json(['answer' => $mac]);
            }
        }
        return $this->json(array("error" => "No matching"));
    }
}
