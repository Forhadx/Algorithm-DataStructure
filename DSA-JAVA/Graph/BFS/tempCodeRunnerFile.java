
            queue.add(node);
            while(!queue.isEmpty()){
                GraphNode currentNode = queue.remove(0);
                currentNode.isVisited = true;
                System.out.print(currentNode.name+" ");
                for(GraphNode neighbor: currentNode.neighbors){
                    if(!neighbor.isVisited){
                        queue.add(neighbor);
                        neighbor.isVisited = true;
                    }
                }
            }