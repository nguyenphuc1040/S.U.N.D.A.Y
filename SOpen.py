def process_string(me):
    if "search" in me:
        me = me.rsplit('search ',1)[1]
        me = me.split()[0]
    elif "open" in me:
        me = me.rsplit('open ',1)[1]
        me = me.split()[0]
    return me
