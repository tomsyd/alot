[global]
    # attributes used in all modi
    footer = attrtriple
    body = attrtriple
    notify_error = attrtriple
    notify_normal = attrtriple
    prompt = attrtriple
    tag = attrtriple
    tag_focus = attrtriple
[help]
    # formatting of the `help bindings` overlay
    text = attrtriple
    section = attrtriple
    title = attrtriple
# mode specific attributes
[bufferlist]
    line_focus = attrtriple
    line_even = attrtriple
    line_odd = attrtriple

[taglist]
    line_focus = attrtriple
    line_even = attrtriple
    line_odd = attrtriple
[search]
    [[threadline]]
        normal = attrtriple
        focus = attrtriple
        # order subwidgets are displayed. subset of {date,mailcount,tags,authors,subject,count}
        # every element listed must have its own subsection below
        parts = string_list(default=None)
        [[[__many__]]]
            normal = attrtriple
            focus = attrtriple
            width = widthtuple(default=None)
            alignment = align(default='right')
    [[__many__]]
        normal = attrtriple(default=None)
        focus = attrtriple(default=None)
        parts = string_list(default=None)
        query = string(default=None)
        tagged_with = force_list(default=None)
        [[[__many__]]]
            normal = attrtriple(default=None)
            focus = attrtriple(default=None)
            width = widthtuple(default=None)
            alignment = align(default='right')
[thread]
    attachment = attrtriple
    attachment_focus = attrtriple
    body = attrtriple
    header = attrtriple
    header_key = attrtriple
    header_value = attrtriple
    [[summary]]
        even = attrtriple
        odd = attrtriple
        focus = attrtriple
[envelope]
    body = attrtriple
    header = attrtriple
    header_key = attrtriple
    header_value = attrtriple
