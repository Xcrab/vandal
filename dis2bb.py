#!/usr/bin/env python3

# Standard lib imports
import fileinput

# Local project imports
from cfglib import ControlFlowGraph
from stacksizeanalysis import run_analysis, block_stack_delta
from destackify import Destackifier

cfg = ControlFlowGraph(fileinput.input())
entry, exit = run_analysis(cfg)
destack = Destackifier()

for block in cfg.blocks:
  print("Entry stack:", entry[block])
  print()
  print(block)
  print(block_stack_delta(block), "stack elements added.")
  print("Exit stack:", exit[block])
  print()

  print("TAC code:\n")
  ops, stack, num = destack.convert_block(block)
  for op in ops:
    print(str(op))
  print("\nNew stack head:", [str(var) for var in stack])
  print("Popped from initial stack:", num)
  print("\n-----\n")
