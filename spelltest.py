from spellcheck import correct,NWORDS
NWORDS=NWORDS
tests1 = { 'access': 'acess', 'accessing': 'accesing', 'accommodation':'accomodation acommodation acomodation', 'account': 'acount'}
 
tests2 = {'forbidden': 'forbiden', 'decisions': 'deciscions descisions', 'supposedly': 'supposidly', 'embellishing': 'embelishing'}

# verbose显示详细信息
# bias加入需要学习的单词，手动纠错
def spelltest(tests, verbose=False, bias=None):
    import time
    n, bad, unknown, start = 0, 0, 0, time.clock()
    if bias:
        for target in tests: NWORDS[target] += bias
    for target,wrongs in tests.items():
        for wrong in wrongs.split():
            n += 1
            w = correct(wrong)
            if w!=target:
                bad += 1
                unknown += (target not in NWORDS)
                if verbose:
                    print ('%r => %r (%d); expected %r (%d)' % (wrong, w, NWORDS[w], target, NWORDS[target]))
    return dict(n=n, pct="{}%".format(int(100. - 100.*bad/n)), bad=bad, unknown=unknown, bias=bias, secs=int(time.clock()-start))
print (spelltest(tests1,True))
print (spelltest(tests2,True))

