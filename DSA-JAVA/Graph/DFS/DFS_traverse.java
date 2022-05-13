
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Stack;

class GraphNode{
    public String name;
    public int index;
    public boolean isVisited = false;

    public ArrayList<GraphNode> neighbors = new ArrayList<GraphNode>();

    public GraphNode(String name, int index){
        this.name = name;
        this.index = index;
    }
}

class Graph{
  ArrayList<GraphNode> nodeList = new ArrayList<GraphNode>();

  public Graph(ArrayList<GraphNode> nodeList) {
    this.nodeList = nodeList;
  }

  public void addUndirectedEdge(int i, int j) {
    GraphNode first = nodeList.get(i);
    GraphNode second = nodeList.get(j);
    first.neighbors.add(second);
    second.neighbors.add(first);
  }



// For printing Graph to the console

  public String toString() {
    StringBuilder s = new StringBuilder();
    for (int i = 0; i < nodeList.size(); i++) {
      s.append(nodeList.get(i).name + ": ");
      for (int j =0; j < nodeList.get(i).neighbors.size(); j++) {
        if (j == nodeList.get(i).neighbors.size()-1 ) {
          s.append((nodeList.get(i).neighbors.get(j).name) );
        } else {
          s.append((nodeList.get(i).neighbors.get(j).name) + " -> ");
        }
      }
      s.append("\n");
    }
    return s.toString();
  }

   // DFS 
   void dfs(String startName){
    Stack<GraphNode> stack = new Stack<>();

    GraphNode node = null ;
    for(GraphNode n: nodeList){
        if(n.name == startName){
            node = n;
        }
    }
    if(node == null){
        System.out.println("Please enter valid string.");
        return;
    }

    stack.push(node);
    while(!stack.isEmpty()){
        GraphNode currentNode = stack.pop();
        currentNode.isVisited = true;
        System.out.print(currentNode.name+" ");
        for(GraphNode neigbor: currentNode.neighbors){
            if(!neigbor.isVisited){
                // System.out.println(neigbor.name);
                stack.push(neigbor);
                neigbor.isVisited = true;
            }
        }
    }

  }

}


public class DFS_traverse {
    public static void main(String[] args) {
        ArrayList<GraphNode> nodelist = new ArrayList<>();

        nodelist.add(new GraphNode("A", 0));
        nodelist.add(new GraphNode("B", 1));
        nodelist.add(new GraphNode("C", 2));
        nodelist.add(new GraphNode("D", 3));
        nodelist.add(new GraphNode("E", 4));
        nodelist.add(new GraphNode("F", 5));
        nodelist.add(new GraphNode("G", 6));

        Graph g = new Graph(nodelist);
        g.addUndirectedEdge(0, 1);
        g.addUndirectedEdge(0, 2);
        g.addUndirectedEdge(1, 3);
        g.addUndirectedEdge(1, 6);
        g.addUndirectedEdge(2, 3);
        g.addUndirectedEdge(2, 4);
        g.addUndirectedEdge(3, 5);
        g.addUndirectedEdge( 5,4);
        g.addUndirectedEdge( 5,6);
        System.out.println(g.toString());

        g.dfs("A");
    }
}
