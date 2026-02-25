;;; Homework 09: Macro

; ANSWER QUESTION wwsd

;;; Required Problems

(define (help-find n lst index)
  (if (null? lst)
      nil
      (if (equal? (car lst) n)
          index
          (help-find n (cdr lst) (+ index 1))
      )
  )
)

(define (find n lst)
  (help-find n lst 0)
)


(define (search lst expr)
  (cond
      ((null? lst) #f)
        ((and (not (pair? lst)) (equal? lst n)) expr)
        ((pair? lst)
         (let ((left (search (car lst) (list 'car expr))))
           (if left
               left
               (search (cdr lst) (list 'cdr expr)))))
        (else #f)))

(define (find-nest n sym)
  (search (eval sym) sym)
)
;; 上面这些是AI写的，自己写绷不住了

(define-macro (my/or operands)
  (cond 
    ((null? operands) #f)
    ((null? (cdr operands)) (car operands))
    (else `(let ((t ,(car operands)))
             (if t
                 t
                 (my/or ,(cdr operands))
              )
            )
    )
  )
)

;; 下面这个也是Claude写的，自己写写错了很多

;; 辅助函数：构造调用fn时的完整参数列表
;; args: 全部参数名列表
;; vals: 要填入的值列表
;; indices: 要填入的位置列表（已排序）
;; 返回：按位置替换后的完整参数列表
(define (build-call-args args vals indices)
  (define (helper args vals indices cur-idx)
    (cond
      ((null? args) '())
      ((and (not (null? indices)) (= cur-idx (car indices)))
       ;; 当前位置是需要填值的位置
       (cons (car vals)
             (helper (cdr args) (cdr vals) (cdr indices) (+ cur-idx 1))))
      (else
       ;; 当前位置保留参数名
       (cons (car args)
             (helper (cdr args) vals indices (+ cur-idx 1))))))
  (helper args vals indices 0))

;; 辅助函数：过滤掉indices指定位置的参数，得到剩余参数列表
(define (remaining-args args indices)
  (define (helper args indices cur-idx)
    (cond
      ((null? args) '())
      ((and (not (null? indices)) (= cur-idx (car indices)))
       ;; 当前位置被固定，跳过
       (helper (cdr args) (cdr indices) (+ cur-idx 1)))
      (else
       ;; 当前位置保留
       (cons (car args)
             (helper (cdr args) indices (+ cur-idx 1))))))
  (helper args indices 0))

;; 宏实现
(define-macro (k-curry fn args vals indices)
  (let* ((args-list args)       ; 参数名列表，如 (a b c d)
         (vals-list vals)       ; 值列表，如 (2 4)
         (idx-list  indices)    ; 位置列表，如 (1 3)
         (rem-args  (remaining-args args-list idx-list))          ; 剩余参数 (a c)
         (call-args (build-call-args args-list vals-list idx-list))) ; 完整调用参数 (a 2 c 4)
    `(lambda ,rem-args (,fn ,@call-args))))


(define-macro (let* bindings expr)
  (if (null? bindings)
      `(let () ,expr) ;这里就是注意一下语法，,expr在`之后，必须要加上才能求值
      `(let (,(car bindings))
            (let* ,(cdr bindings) ,expr))
  )
)

;;; Just For Fun Problems
; 下面这些写不动了

; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)
