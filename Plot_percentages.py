def show_percentages(plot,lenght):
    for p in plot.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/float(lenght))
        x = p.get_x() + p.get_width()/2
        y = 1.02*p.get_height()
        plot.annotate(percentage, (x, y),ha='center',fontsize = 16)
        