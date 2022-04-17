def get_text_by_selector(container, selector):
    elem = container.find_elements_by_class_name(selector)

    if len(elem) > 0:
        return next(iter(elem)).text.replace('\n',' ').strip()
    else: 
        print(f'Missing value for selector {selector}')
        return ''