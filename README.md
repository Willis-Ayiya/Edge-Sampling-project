EDGE SAMPLING FOR GRAPH OPTIMIZATION
This project explores an edge sampling technique for reducing graph complexity while preserving connectivity and key spectral properties. The goal is to make large networks lighter and more efficient for tasks such as IoT sensor data and communication networks

How It Works
1. Graph Generation– A random geometric graph is built using networkx, simulating nodes connected by proximity.  
2.Node Signals – Each node is assigned a random value 
3. Edge Smoothness – For every edge (i,j), we compute s(e) = (x_i - x_j)^2. Lower values mean smoother (more similar) signals.  
4.Sampling – Keep the lowest smoothness edges  and add  edges to ensure the graph stays connected.  
5.Visualization– Original graph is drawn in gray, sampled edges in red. Results are saved as output_graph.png and output_graph_annot.png. 


How we ran the project.
1. Create virtual environment
python -m venv venv
venv\Scripts\activate     

 2. Install the requirements.
pip install -r requirements.txt
3. Run the demo 
python main.py it savesthe output
