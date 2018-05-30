from .utils import get_effects_summary, get_signed_number


def get_event_details(event):
    event.effects_summary = get_effects_summary(event)
    l = []
    if event.fame_increment != 0:
        l.append('fame %s' % get_signed_number(event.fame_increment)['s'])
    if event.infamy_increment != 0:
        l.append('infamy %s' % get_signed_number(event.infamy_increment)['s'])
    if event.unrest_increment != 0:
        l.append('unrest %s' % get_signed_number(event.unrest_increment)['s'])
    if event.treasury_increment != 0:
        l.append('treasury %s' % get_signed_number(event.treasury_increment)['s'])
    event.resolution = ', '.join(l)
    return {'event': event}
