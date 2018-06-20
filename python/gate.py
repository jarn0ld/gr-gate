#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class gate(gr.basic_block):
    """
    docstring for block gate
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="gate",
            in_sig=[numpy.complex64, numpy.complex64, numpy.uint8],
            out_sig=[numpy.complex64, numpy.complex64])

        self.frame_len = 2000
        self.state = 0
        self.frame_cnt = 0

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):

        gate = input_items[2]
        ch0 = input_items[0]
        ch1 = input_items[1]
        out_ch0 = []
        out_ch1 = []

        for i in range(len(output_items[0])):
            if self.state == 0:
                if gate[i] > 0:
                    self.state = 1
                    self.frame_cnt = 0

            if self.state == 1:
                self.frame_cnt += 1
                out_ch0.append(ch0[i])
                out_ch1.append(ch1[i])
                if self.frame_cnt > self.frame_len:
                    self.state = 0

        self.consume(0, len(output_items[0]))
        self.consume(1, len(output_items[0]))
        self.consume(2, len(output_items[0]))

        output_items[0][:len(out_ch0)] = out_ch0
        output_items[1][:len(out_ch1)] = out_ch1


        return len(out_ch0)

