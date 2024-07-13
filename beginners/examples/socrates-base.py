import cvc5
from cvc5 import Kind, ProofRule

def printProof(proof, indent=0):
  rule = proof.getRule()
  result = proof.getResult()
  childrenProofs = proof.getChildren()
  toPrint = "\n{}{} :".format(" " * indent, result)
  if not childrenProofs:
      return toPrint + " " + str(rule)[10:]
  indent += 2
  toPrint += "\n{}({}".format(" " * indent, str(rule)[10:])
  for cPf in childrenProofs:
    toPrint += printProof(cPf, indent + 2)
  return toPrint + ")".format(" " * indent)

s = cvc5.Solver()

s.setOption("produce-proofs", "true")
s.setOption("proof-granularity", "theory-rewrite")
s.setOption("dag-thresh", "0")

S = s.declareSort("S", 0)
Bool = s.getBooleanSort()
Human = s.declareFun("Human", [S], Bool)
Mortal = s.declareFun("Mortal", [S], Bool)
Socrates = s.mkConst(S, "Socrates")

x = s.mkVar(S, "x")
s.assertFormula(s.mkTerm(Kind.FORALL, s.mkTerm(Kind.VARIABLE_LIST, x),
                         s.mkTerm(Kind.IMPLIES,
                                  s.mkTerm(Kind.APPLY_UF, Human, x),
                                  s.mkTerm(Kind.APPLY_UF, Mortal, x))))
s.assertFormula(s.mkTerm(Kind.APPLY_UF, Human, Socrates))
s.assertFormula(s.mkTerm(Kind.NOT, s.mkTerm(Kind.APPLY_UF, Mortal, Socrates)))

print(s.checkSat())
print("The core is:\n{}"
      .format("\n".join("   - %s" % a for a in s.getUnsatCore())))

proof = s.getProof()[0]
print("--\nThe proof is:\n{}".format(printProof(proof.getChildren()[0])))
