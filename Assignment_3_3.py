{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Score: 0.85\n",
      "B\n"
     ]
    }
   ],
   "source": [
    "x = input(\"Enter Score: \")\n",
    "if float(x) >= 0.9:\n",
    "    print('A')\n",
    "elif float(x) >= 0.8:\n",
    "        print('B')\n",
    "elif float(x) >= 0.7:\n",
    "        print('C')\n",
    "elif float(x) >= 0.6:\n",
    "        print('D')\n",
    "elif float(x) <= 0.6:\n",
    "        print('F')\n",
    "elif float(x) <= 0.0:\n",
    "    print ('Error below acceptance')\n",
    "else:\n",
    "    print ('Error out of range')"
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
