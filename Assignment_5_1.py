{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 5\n",
      "Enter a number: 4\n",
      "Enter a number: dgr\n",
      "Invalid input\n"
     ]
    }
   ],
   "source": [
    "num=0\n",
    "tot=0.0\n",
    "while True :\n",
    "    sval = input('Enter a number: ')\n",
    "    if sval == 'done' :\n",
    "        break\n",
    "    try:\n",
    "        fval = float(sval)\n",
    "    except:\n",
    "        print('Invalid input')\n",
    "        continue\n",
    "    #print(fval)\n",
    "    num= num + 1\n",
    "    tot = tot + fval\n",
    "\n",
    "#print('ALL DONE')\n",
    "print(tot, num, tot/num)"
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
 "nbformat_minor": 4
}
