
def component2json(component):
    """ Recursive function that is going to do the work converting from dash component to json representation"""
    if isinstance(component, list):
        return [component2json(child) for child in component]

    if hasattr(component, 'to_plotly_json'):
        component_dict = component.to_plotly_json()
        if 'props' in component_dict:
            component_dict['props'] = {
                k: component2json(v) for k, v in component_dict['props'].items()
            }
        return component_dict

    return component
