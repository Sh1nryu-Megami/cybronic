<?php

/**
 * @OA\Info(title="API Documentation", version="1.0")
 */

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Predis;

class GetAllFromRedis extends AbstractController
{
    /**
     * Retrieves all users from Redis.
     * 
     * This endpoint retrieves all users stored in Redis.
     *
     * @OA\Get(
     *     path="/api/getall",
     *     summary="Retrieve all users from Redis",
     *     @OA\Response(response="200", description="Successful operation")
     * )
     * @OA\Post(
     *     path="/api/getall",
     *     summary="Retrieve all users from Redis",
     *     @OA\Response(response="200", description="Successful operation")
     * )
     * 
     * @Route("/api/getall", methods={"GET", "POST"})
     * @OA\PathItem()
     */
    #[Route('api/getall', methods: ['GET', 'POST'])]
    public function getAll(): Response
    {
        $redis = new Predis\Client();
        $keys = $redis->keys('*');
        $posts = array();
        foreach ($keys as $key) {
            $posts[] = array('mac' => $key) + $redis->hgetall($key);
        }
        return $this->json($posts);
    }
}