import sand.cytoscape.themes.colors as c
import sand.cytoscape.themes.label_positions as p


settings = {
    # node style
    'NODE_TRANSPARENCY': 255,
    'NODE_SIZE': 25,
    'NODE_BORDER_WIDTH': 4,
    'NODE_BORDER_PAINT': c.BRIGHT_GREEN,
    'NODE_FILL_COLOR': c.DARK_GREEN,
    'NODE_SELECTED_PAINT': c.BRIGHT_YELLOW,

    # node label style
    'NODE_LABEL_COLOR': c.BRIGHT_GRAY,
    'NODE_LABEL_FONT_SIZE': 16,
    'NODE_LABEL_POSITION': p.LOWER_RIGHT,

    # edge style
    'EDGE_TRANSPARENCY': 255,
    'EDGE_WIDTH': 2.5,
    'EDGE_LINE_TYPE': 'SOLID',
    'EDGE_STROKE_SELECTED_PAINT': c.BRIGHT_YELLOW,
    'EDGE_STROKE_UNSELECTED_PAINT': c.BRIGHT_GRAY,
    'EDGE_TARGET_ARROW_UNSELECTED_PAINT': c.BRIGHT_GRAY,
    'EDGE_TARGET_ARROW_SHAPE': 'DELTA',

    # network style
    'NETWORK_BACKGROUND_PAINT': c.DARK_GRAY
}