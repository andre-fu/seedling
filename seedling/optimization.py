from typing import Callable, List
import random
class Optimization:

    def __init__(self):
        self.aa = ['A', 'R', 'N', 'D', 'C', 'Q' ,'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    def genetic_algorithm(self, dna_sequence: str, minimize: bool, pool_size: int, fitness: Callable[[str], float], bad_idx: List[int]) -> str:
        """Generate a Genetic Algorithm to return the top optimized amino acid sequence
        
        Arguments:
            dna_sequence {str} -- Amino Acid Sequence for a Protein
            minimize {bool} -- To Minimize - TRUE, to maximize - FALSE
            pool_size {int} -- How big the gene pool is
            fitness {Callable[[str], float]} -- Function to evaluate all amino acid sequences
            bad_idx {List[int]} -- List of indicies to not touch
        
        Returns:
            str -- The Amino Acid sequence of the optimized sequence
        """
        
        # #POP_SIZE = 100
        # POP: List[int] = []
        # i: int = 0
        # while i < pool_size:
        #     newDna = dna_sequence
        #     f = True 
        #     while f == True:
        #         idx = random.randint(0, len(dna_sequence)-1 )
        #         if (idx in bad_idx):
        #             continue
        #         else: 
        #             break
        #     newDna = list(newDna)
        #     newDna[idx] = changes[random.randint(0, len(changes)-1)]
        #     newDna = ''.join(newDna)
        #     POP.append(newDna)
        #     i += 1
        # #now you have a 100 random mutations of petase
        # genepool = []
        # for i in range(0, len(POP)):
        #     fit = fitness(POP[i]) 
        #     sim = self._similarity(POP[i])
        #     candidate = {'dna': POP[i], 'fitness': fit, 'similarity': sim}
        #     genepool.append(candidate)
        return 'hellowlrd'
    
    def _mutate(self, parent1: dict, parent2: dict, no_mutate: List[int], fitness: Callable[[str], float]) -> dict:
        """Mutates two 'dna' sequences together
        
        Arguments:
            parent1 {dict} -- {'dna': str, 'fitness': float}
            parent2 {dict} -- {'dna': str, 'fitness': float}
            no_mutate {List[int]} -- List of indicies not to mutate
            fitness {Callable[[str], float]} -- Function to evaluate the fitness of a 'dna' string
        
        Returns:
            dict -- {'dna': mutated sequence (str), 'fitness': numerical evaluation (float)}
        """
        aa = ['A', 'R', 'N', 'D', 'C', 'Q' ,'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
        child_dna = parent1['dna']

        f = True
        while f == True: 
            start: int = random.randint(0, len(parent2['dna'] - 1))
            stop: int = random.randint(0, len(parent2['dna'] - 1))
            if (start) in no_mutate:
                continue
            if (stop) in no_mutate:
                continue 
            else:
                f = False
                break
        
        if (start or stop) in no_mutate:
            return {'error': 'Something is wrong please submit a PR for this code'}
        if start > stop:
            stop, start = start, stop
        child_dna = list(child_dna)
        parent2['dna'] = list(parent2['dna'])
        child_dna[start:stop] = parent2['dna'][start:stop]
        child_dna = ''.join(child_dna)
        parent2['dna'] = ''.join(parent2['dna'])

        f = True 
        while f == True:
            charpos: int = random.randint(0, len(child_dna) - 1)
            if (charpos in no_mutate):
                continue
            else: 
                f= False
                break
        child_dna = list(child_dna)
        child_dna[charpos] = self.aa[random.randint(0, len(changes)-1)]
        child_fitness = fitness(child_dna) #remove target 
        child_dna[start:stop] = parent2['dna'][start:stop]
        child_dna = ''.join(child_dna)

        return({'dna': child_dna, 'fitness': child_fitness})

    def _random_parent(self, genepool: List[dict], pop_size: int) -> dict:
        rng = random.randint(0, pop_size -1)
        return(genepool[rng])
    def _fitness(self, dna: dict, keys: dict):
        """Calculates the sum of the numerical evaluation - could use your own fitness function
        
        Arguments:
            dna {dict} -- dna dictionary for calculation
            keys {dict} -- guide keys for the summation (whimely-white scale used)
        
        Returns:
            float -- the summation of the numerical value of the elements for amino acids
        """
        sum:float = 0
        for i in range(0, len(dna)):
            sum += float(keys[dna[i]][1])
        return sum
    
    def _similarity(seq:str, compare:str):
        """Calculates the similarity between a seqeunce and a wild-type sequence 
        
        Arguments:
            seq {str} -- the novel seqeuence to compare against 
            compare {str} -- the wild-type sequence
        
        Returns:
            float -- the percentage similarity between the sequences
        """
        tally:int = 0
        for i in range(0, len(compare)):
            if seq[i] == compare[i]:
                tally += 1
        return tally/len(compare) * 100
    
    
    
    
