// callback to deregister vclicktable
function zoomToNode(cy, nodeId) {
    var node = cy.getElementById(nodeId);
    if (node && node.length > 0) {
        cy.animate({
            fit: {
                eles: node,
                padding: 20
            },
            duration: 500,
            easing: 'ease-in-out'
        });
    } else {
        console.warn('Node not found:', nodeId);
    }
}

