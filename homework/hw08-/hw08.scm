;;; Homework 08: Scheme

;;; Required Problems

;;; 不会写就反复读：https://sicp.pascal-lab.net/2025/labs/lab08/2.html

(define (square x) (* x x))

;; Problem 1: Quick Pow

(define (quick-pow base exp)
  (if (= 1 base) 
      1
      (if (= 0 exp)
          1
          (if (even? exp)
              (square (quick-pow base (/ exp 2)))
              (* base (quick-pow base (- exp 1))))))
)

;; Problem 2: Quicker Pow
;; 按照题目要求，这个必须是尾递归的


(define (help base exp res)
    (if (= 0 exp)
        res
        (if (even? exp)
            (help base (/ exp 2) (* res (quick-pow base (/ exp 2)))) ;其实不是很确定调用quick-pow能不能算尾递归
            (help base (- exp 1) (* res base))
            )
    )
)
;; 以上这个是我自己写的

(define (helper base exp acc)
    (cond ((= exp 0) acc)
          ((even? exp)
           (helper (* base base) (/ exp 2) acc))  ; 尾递归：base² 的 exp/2 次方
          (else
           (helper base (- exp 1) (* acc base)))))  ; 尾递归：累积 base
  (helper base exp 1)
;; 以上这个是Claude给的修改意见

(define (quicker-pow base exp)
  (help base exp 1)
)


;; Problem 3: Find

(define (find predicate lst)
  (if (null? lst) ;; 这里语法注意一下
      #f
      (if (predicate (car lst))
            (car lst)
            (find predicate (cdr lst))
      )
  )
)

;; Problem 4: Count Change III

(define (help-mc num res)
  (map (lambda (res) (cons num res)) res)) ;; 把first添加到每个数组的最前面

(define (make-change total biggest)
  (
    cond 
      ((= total 0) (list nil))
      ((or (< total 0) (= biggest 0)) nil)
      (else (
        append
          (help-mc biggest (make-change (- total biggest) biggest)) ;; biggest被添加了
          (make-change total (- biggest 1)) ;;当前biggest不添加, -1再讨论
        )
      )
  )
)

;; Problem 5: Enumerate

(define (help-en lst index)
  (if (null? lst)
    nil
    (cons (cons index (car lst)) ;;这样已经能够添加点对了
          (help-en (cdr lst) (+ index 1))
    )
  )
)

(define (enumerate lst)
  (help-en lst 0)
)

;; Problem 6: Substitute

(define (find-su bindings key) 
  (if (null? bindings)
    #f
    (if (equal? (car (car bindings)) key)
      (cdr (car bindings))
      (find-su (cdr bindings) key)
    )
  )
)


(define (substitute bindings s)
  (cond 
    ((null? s) '()) ;; 如果是空列表，就返回nil

    ((pair? (car s))
      (cons (substitute bindings (car s))
            (substitute bindings (cdr s)) 
            ; 递归处理，把前面的列表替换后追加到后面的列表替换后
      )
    )

    (else
      (let ((replacement (find-su bindings (car s))))
        (if replacement
          (cons replacement (substitute bindings (cdr s)))
          (cons (car s) (substitute bindings (cdr s)))
        )
      )
    )
  )
)

;; Problem 7: Tree in Scheme

(define (tree label branches)
  (cons label branches) 
)

(define (label t)
  (if (equal? t nil)
      (nil)
      (car t) 
  )
)

(define (branches t)
  (if (equal? t nil)
      (nil)
      (cdr t) 
  )
)

(define (is-leaf t)
  (equal? (branches t) nil)
)

; A tree for test

(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 5 nil)
        (tree 6 (list
          (tree 8 nil)))))
    (tree 3 nil)
    (tree 4
      (list
        (tree 7 nil))))))

;; Problem 8: Label Sum

(define (label-sum t)
  (if (is-leaf t)
      (label t)
      (+ (label t)
         (apply + (map label-sum (branches t))))
  )
)
;; (map label-sum (branches t)) 对每个子树调用 label-sum，得到列表 '(sum1 sum2 ...)
;; (apply + '(sum1 sum2 ...)) 等价于 (+ sum1 sum2 ...)

;;; Just For Fun Problems

;; Problem 9: Derive

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand (already defined for sum).
; (define (first-operand p) (cadr p))
; (define (second-operand p) (caddr p))

;; Problem 9.1: Derive Sum

(define (derive-sum expr var)
  'YOUR-CODE-HERE
)

;; Problem 9.2: Derive Product

(define (derive-product expr var)
  'YOUR-CODE-HERE
)

;; Problem 9.3: Make Exp

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  'YOUR-CODE-HERE
)

(define (exp? exp)
  'YOUR-CODE-HERE
)

; Some expressions for test
(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

;; Problem 9.4: Derive Exp

(define (derive-exp exp var)
  'YOUR-CODE-HERE
)
