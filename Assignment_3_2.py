{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Hours: 45\n",
      "Enter Rate: 10.5\n",
      "Pay: 498.75\n"
     ]
    }
   ],
   "source": [
    "hrs = input(\"Enter Hours: \")\n",
    "rate = input(\"Enter Rate: \")\n",
    "xh = float(hrs)\n",
    "yh = float(rate) \n",
    "if xh > 40:\n",
    "    xhyh= xh * yh\n",
    "    xhyh= ((xh-5)*yh) + ((xh - 40) * (yh * 1.5)) \n",
    "else:\n",
    "    xhyh= xh * yh\n",
    "print(\"Pay:\", xhyh)"
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
