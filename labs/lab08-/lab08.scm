;;; Lab08: Scheme

(define (over-or-under a b)
  (if (> a b) 1 (if (= a b) 0 -1))
)


(define (make-adder n)
  (lambda (x) (+ x n))
)


(define (composed f g)
  (lambda (x) (f (g x)))
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if (= 0 b) 
      a
      (gcd b (modulo a b))
  ) 
)


(define lst
  (cons (cons 1 nil) 
        (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))
)

(define lst2 (list (list 1) 2 (list 3 4) 5)) ; 另一种表达

(define (ordered s)
  (if (or (null? s) (null? (cdr s)))
      #t
      (and (<= (car s) (car (cdr s)))
           (ordered (cdr s))
      )
  )
)
