<?php

function BFS($n, $graph, $u, $v)
{
    $keys = array_keys($graph);
    $dist = array_fill_keys($keys, $n);
    $dist[$u] = 0;
    $path = array_fill_keys($keys, -1);
    $queue = new SplQueue();
    $queue->enqueue($u);
    while (!$queue->isEmpty()) {
        $curr_vert = $queue->dequeue();
        foreach ($graph[$curr_vert]['adjacent'] as $next_vert) {
            if ($dist[$next_vert] > $dist[$curr_vert] + 1) {
                $dist[$next_vert] = $dist[$curr_vert] + 1;
                $path[$next_vert] = $curr_vert;
                $queue[] = $next_vert;
            }
        }
    }

    if ($dist[$v] == $n) {
        return -1;
    } else {
        $res = array();
        while ($v != -1) {
            $res[] = $v;
            $v = $path[$v];
        }
        return $res;
    }
}
