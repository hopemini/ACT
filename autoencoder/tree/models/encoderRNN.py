import os
import sys

import torch
import torch.nn as nn

from models.baseRNN import BaseRNN

class EncoderRNN(BaseRNN):

    def __init__(self, vocab_size, max_len, hidden_size,
                 embedding_size, input_dropout_p=0, dropout_p=0, pos_embedding_size=None, pos_embedding=None,
                 n_layers=1, bidirectional=False, rnn_cell='lstm', variable_lengths=False,
                 embedding=None, update_embedding=True):
        super(EncoderRNN, self).__init__(vocab_size, max_len, hidden_size,
                input_dropout_p, dropout_p, n_layers, rnn_cell)

        self.variable_lengths = variable_lengths
        # print(embedding_size)
        self.embedding = nn.Embedding(vocab_size, 64)
        if embedding is not None:
            self.embedding.weight = nn.Parameter(embedding)
        self.embedding.weight.requires_grad = update_embedding
        self.pos_embedding = pos_embedding
        #if self.pos_embedding != None:
        #    self.rnn = self.rnn_cell(embedding_size+pos_embedding_size, hidden_size, n_layers,
        #                         batch_first=True, bidirectional=bidirectional, dropout=dropout_p)
        #else:
        #    self.rnn = self.rnn_cell(embedding_size, hidden_size, n_layers,
        #                         batch_first=True, bidirectional=bidirectional, dropout=dropout_p)
        self.childsumtreelstm = nn.LSTMCell(64, hidden_size)

    def forward(self, input_var, nodes, input_lengths=None):
        batch_size = input_var.size(0)
        seq_len = input_var.size(1)
        # print("input_var: {}".format(input_var.shape))
        # print("nodes: {}".format(nodes.shape))

        embedded = self.embedding(input_var)
        # print("embedded: {}".format(embedded.shape))

        current_node = 0

        hidden = torch.tensor([]).cuda()
        context = torch.tensor([]).cuda()
        output = torch.tensor([]).cuda()
        # print("input_var shape: {}".format(input_var))
        # print("nodes shape: {}".format(nodes))
        for emb, node in zip(embedded, nodes):
            # print("emb shape: {}".format(emb.shape))
            # print("nodes shape: {}".format(node))
            max_nodeNum = max(node)
            # hds = torch.tensor([]).cuda()
            # print("max_nodeNum: {}".format(max_nodeNum))
            for current_node in range(max_nodeNum, 1, -1):
                # print("current_node: {}".format(current_node))
                # print("emb: {}".format(emb.shape))
                node_t = node.unsqueeze(-1).repeat(1,64)
                # print("node_t: {}".format(node_t.shape))
                # print("node_t.eq(current_node): {}".format(node_t.eq(current_node).shape))
                # print("emb shape: {}".format(emb.shape))

                tmp = emb.masked_select(node_t.eq(current_node)).view(-1, emb.size(1))
                # print("tmp: {}".format(tmp.shape))
                for j, tens in zip(range(len(tmp)), tmp):
                    tens = tens.unsqueeze(0)
                    # print("tens: {}".format(tens.shape))
                    if j == 0:
                        h, c = self.childsumtreelstm(tens)
                    else:
                        h, c = self.childsumtreelstm(tens, (h, c))
                    # hds = torch.cat((hds, h), dim=0)
                    # print("h: {}".format(h.shape))
                    # print("c: {}".format(c.shape))
            hidden = torch.cat((hidden, h), dim=0)
            context = torch.cat((context, c), dim=0)
            # output = torch.cat((output, hds.unsqueeze(0)), dim=0)

        # print(output.shape)
        # print(hidden.shape)
        hiddens = (hidden.unsqueeze(0), context.unsqueeze(0))
        # print(hiddens)

        return output, hiddens
