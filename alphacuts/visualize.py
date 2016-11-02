#!/usr/bin/python2.7
__author__ = 'tsabsch <tim@sabsch.com>'

import bisect
import matplotlib.pyplot as plt

def horizontal_view(alpha_cuts):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot each alpha cut range in the dict
    for degree, alpha_cut in alpha_cuts.iteritems():
        for iv in acut:
            ax.plot(iv, [degree,degree], marker='.', color='black')

    # set y axis to interval [0,1]
    ax.set_ylim([0,1.1])
    ax.set_yticks(alpha_cuts.keys())

    return fig

def upper_envelope(alpha_cuts):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    xs = list()
    ys = list()
    tmp_steps = list()

    for degree, cuts in alpha_cuts.iteritems():

        # insert temporary steps
        for x in tmp_steps:
            i = bisect.bisect_left(xs, x)
            xs.insert(i, x)
            ys.insert(i, degree)
        tmp_steps = list()

        for (start, end) in cuts:
            if end not in xs:
                # insert new (down) step
                i = bisect.bisect(xs, end)
                xs.insert(i, end)
                ys.insert(i, degree)

            if start in xs:
                if start == end:
                    # special case: peak
                    tmp_steps += [start]
                else:
                    # update step
                    i = xs.index(start)
                    ys[i] = degree
            else:
                # new up step detected, put on hold until degree is determined
                tmp_steps += [start]

    ax.step(xs,ys)
    ax.set_ylim([0,1.1])
    ax.set_yticks(alpha_cuts.keys())
    return fig

def visualize(alpha_cuts, kind='horizontal_view'):
    if kind == 'horizontal_view':
        fig = horizontal_view(alpha_cuts)
    if kind == 'upper_envelope':
        fig = upper_envelope(alpha_cuts)

    plt.show()

def visualize_x(alpha_cuts, x):
    # TODO: implement
    pass
