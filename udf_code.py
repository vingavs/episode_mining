def winepi_srinivas(sequence, window_size, frequency_threshold):
    Te = int(min(sequence[:,0]))
    Ts = int(max(sequence[:,0]))
    size1 = np.size(sequence,0)
    
    sequence2 = np.zeros((Ts-Te+1+2*(window_size-1),2))
    
    for i in range(0,Ts-Te+1+2*(window_size-1)):
        sequence2[i,0]=int(Te-window_size+1+i)
    
    for j in range(0,size1):
        for i in range(0,Ts-Te+1+2*(window_size-1)):
            if(sequence2[i,0]==sequence[j,0]):
                sequence2[i,1]=int(sequence[j,1])
                break
            
    episode_max = int(max(sequence2[:,1]))
    window_total =  Ts-Te+window_size
    
    freq_1d = np.zeros((episode_max,window_total))
    freq_2d = np.zeros((episode_max,episode_max,window_total))
    freq_3d = np.zeros((episode_max,episode_max,episode_max,window_total))
    
    for h in range(1,episode_max+1):
        for i in range(0,Ts-Te+window_size):
            for j in range(i,i+window_size):
                    if(sequence2[j,1]==h):
                        freq_1d[h-1,i]=1
                        break
                    
    for h1 in range(1,episode_max+1):
        for h2 in range(1,episode_max+1):     
            for i in range(0,Ts-Te+window_size):
                find = 0
                for j in range(i,i+window_size):
                    for k in range(i,i+window_size):
                        if((k>j)&(sequence2[j,1]==h1)&(sequence2[k,1]==h2)):
                            freq_2d[h1-1,h2-1,i]=1
                            find = 1
                            break
                    if(find == 1):
                        break
                
    for h1 in range(1,episode_max+1):
        for h2 in range(1,episode_max+1):
            for h3 in range(1,episode_max+1):
                for i in range(0,Ts-Te+window_size):
                    find = 0
                    for j in range(i,i+window_size):
                        for k in range(i,i+window_size):
                            for l in range(i,i+window_size):
                                if((l>k)&(k>j)&(sequence2[j,1]==h1)&(sequence2[k,1]==h2)&(sequence2[l,1]==h3)):
                                    freq_3d[h1-1,h2-1,h3-1,i]=1
                                    find = 1
                                    break
                            if(find == 1):
                                break
                        if(find == 1):
                            break
   
    count_1d = np.zeros(episode_max,)
    count_2d = np.zeros((episode_max,episode_max))
    count_3d = np.zeros((episode_max,episode_max,episode_max))
                      
    for i in range(0, episode_max):
        for j in range(0, window_total):
            count_1d[i]=count_1d[i]+freq_1d[i,j]
    
    for i in range(0, episode_max):
        for j in range(0, episode_max):
            for k in range(0, window_total):
                count_2d[i,j]=count_2d[i,j]+freq_2d[i,j,k]
                 
    for i in range(0, episode_max):
        for j in range(0, episode_max):
            for k in range(0,episode_max):
                for l in range(0, window_total):
                    count_3d[i,j,k]=count_3d[i,j,k]+freq_3d[i,j,k,l]
                
    count2_1d = np.zeros(episode_max,)
    count2_2d = np.zeros((episode_max,episode_max))
    count2_3d = np.zeros((episode_max,episode_max,episode_max))        
               
    for i in range(0, episode_max):
        count2_1d[i] = count_1d[i]/window_total                   
                    
    for i in range(0, episode_max):
        for j in range(0, episode_max):
            count2_2d[i,j]=count_2d[i,j]/window_total
                 
    for i in range(0, episode_max):
        for j in range(0, episode_max):
            for k in range(0,episode_max):
                count2_3d[i,j,k]=count_3d[i,j,k]/window_total
                
    frequent_episodes = np.zeros((1,4))
    
    for i in range(0, episode_max):
        if(count2_1d[i] >= frequency_threshold):
            c = count2_1d[i]
            addition = np.array([[i+1,0,0,c]])
            frequent_episodes=np.append(frequent_episodes,addition, axis = 0)
            
    for i in range(0, episode_max):
        for j in range(0, episode_max):
            if(count2_2d[i,j] >= frequency_threshold):
                c = count2_2d[i,j]
                addition = np.array([[i+1,j+1,0,c]])
                frequent_episodes=np.append(frequent_episodes,addition, axis = 0)
                
    for i in range(0, episode_max):
        for j in range(0, episode_max):
            for k in range(0,episode_max):
                if(count2_3d[i,j,k] >= frequency_threshold):
                    c = count2_3d[i,j,k]
                    addition = np.array([[i+1,j+1,k+1,c]])
                    frequent_episodes=np.append(frequent_episodes,addition, axis = 0)
                
    frequent_episodes2=frequent_episodes[1:np.size(frequent_episodes,0),:]   
    return frequent_episodes2
