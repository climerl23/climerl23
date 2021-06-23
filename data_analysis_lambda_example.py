{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b8fbaf9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Dr. Brooks', 'Dr. Collins-Thompson', 'Dr. Vydiswaran', 'Dr. Romero']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']\n",
    "\n",
    "#def split_title_and_name(person):return person.split()[0] + ' ' + person.split()[-1]\n",
    "\n",
    "#option 1\n",
    "#for person in people: print(split_title_and_name(person) == (lambda person:???))\n",
    "\n",
    "#option 2\n",
    "#list(map(split_title_and_name, people)) == list(map(???))\n",
    "\n",
    "\n",
    "people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']\n",
    "\n",
    "def split_title_and_name(person):\n",
    "    return person.split()[0] + ' ' + person.split()[-1]\n",
    "\n",
    "#option 1\n",
    "for person in people:\n",
    "    print(split_title_and_name(person) == (lambda person:person.split()[0] + ' ' + person.split()[-1])(person))\n",
    "\n",
    "#option 2\n",
    "list(map(split_title_and_name, people)) == list(map(lambda person: person..split()[0] + '  ' + person.split()[-1])(person))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
