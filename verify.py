def verify():
    ref = open('output.txt','r')
    res = open('output_result.txt','r')
    for ref_line,res_line in zip(ref,res):
        # Strip to get rid of '\n' 
        if ref_line.strip('\n') != res_line.strip('\n'):
            print('Not equal')
            return False
    print('all success')
    ref.close()
    res.close()
    return True

if __name__ == "__main__":
    verify()