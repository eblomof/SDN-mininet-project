
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def setup_topology():
    net = Mininet(controller=RemoteController)
    
    # Add a remote controller
    controller = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
    
    # Add a switch
    switch = net.addSwitch('s1')
    
    # Add hosts
    host1 = net.addHost('h1', ip='10.0.0.1')
    host2 = net.addHost('h2', ip='10.0.0.2')
    host3 = net.addHost('h3', ip='10.0.0.3')
    
    # Add links
    net.addLink(host1, switch)
    net.addLink(host2, switch)
    net.addLink(host3, switch)
    
    # Start the network
    net.start()
    
    print("Network setup complete. You can now use the Mininet CLI.")
    CLI(net)
    
    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_topology()
